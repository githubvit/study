//  头文件

#ifndef UICANVASITEMBASE_H
#define UICANVASITEMBASE_H

#include <QObject>
#include <QGraphicsItem>
#include <QPixmap>
#include <QGraphicsObject>

class UICanvasItemBase : public QObject, public QGraphicsItem
{
    Q_OBJECT

public:
    enum ItemOperator
    {
        t_none,
        t_move,
        t_resize,
        t_rotate
    };

    UICanvasItemBase(QGraphicsItem* parentItem = nullptr);
    ~UICanvasItemBase() override;

    // 设置改变大小相关属性
    void setItemResizeable(bool resizeable);
    void setItemResizeRatio(bool resizeRation, qreal rationValue);

private:
    // 初始化Icon
    void initIcon(void);

    static QImage m_closeIcon;
    static QImage m_resizeIcon;
    static QImage m_rotateIcon;

    QPixmap m_closePixmap;
    QPixmap m_resizePixmap;
    QPixmap m_rotatePixmap;

    // 设置是否能够更改尺寸
    bool m_isResizeable = true;
    bool m_isRatioScale = true;
    qreal m_ratioValue = 1.0;

protected:
    QRectF boundingRect() const override;
    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget) final;
    QPainterPath shape() const override;

    void mousePressEvent(QGraphicsSceneMouseEvent *event) override;
    void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override;
    void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override;

    QVariant itemChange(QGraphicsItem::GraphicsItemChange change, const QVariant &value) override;

    // 自定义元素绘制
    virtual void customPaint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget);

    QSize m_size;
    ItemOperator m_itemOper = t_none;

    // 获取自定义绘制所需要的矩形
    QRectF getCustomRect(void) const;

protected:
    // 处理Item上的类型
    virtual void mouseMoveMoveOperator(const QPointF& scenePos, const QPointF& loacalPos);
    virtual void mouseMoveResizeOperator(const QPointF& scenePos, const QPointF& loacalPos);
    virtual void mouseMoveRotateOperator(const QPointF& scenePos, const QPointF& loacalPos);

    QPointF m_pos;              // 本地所坐标点击的点
    QPointF m_pressedPos;       // 场景坐标点击的点
    QPointF m_startPos;         // Item再场景坐标的起始坐标
    QTransform m_transform;     // 变换矩阵
    qreal m_rotate = 0.0;       // 当前旋转角度

signals:
    void onClickedCopyItem(void);

private:
    int m_nInterval = 20;
    int m_nEllipseWidth = 12;    // 半径

    // 画笔设置
    QColor m_cPenColor;
    int m_nPenWidth = 1;
    // 画刷设置
    QColor m_cBrushColor;
};
#endif